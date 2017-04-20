var board_to_str = function(board) {
    return board.reduce(function(str, row) {
        return str + row.reduce(function(row_str, cell){
            return row_str + cell;
        }, '');
    }, '');
}

var tic_tac = new Vue({
    el: "#tic-tac-toe",
    delimiters: ["[[", "]]"],
    data: {
        moves: 0,
        player: 1,
        board: [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        finished: false
    },
    http: {
    },
    methods: {
        move: function(row_index, column_index) {
            if(this.board[row_index][column_index] == 0 && !this.finished)
            {
                var row = this.board[row_index]
                row[column_index] = this.player;
                this.board.splice(row_index, 1, row);
                p = this.player == 1 ? 2 : 1;
                board_str = board_to_str(this.board);
                var scope = this;
                this.moves += 1;
                $('#wait-modal').modal();
                this.$http.get('/Tic-Tac-Toe', { params: {
                    'player': p,
                    'board': board_str
                }}).then(function(response){
                    return response.json();
                }).then(function(json) {
                    var stop = false;
                    for(var i = 0; i < scope.board.length && !stop; i++){
                        row = scope.board[i];
                        for(var j = 0; j < row.length && !stop; j++){
                            if(scope.board[i][j] != json.board[i][j]){                                
                                row[j] = json.board[i][j];
                                scope.board.splice(i, 1, row);
                                this.moves += 1;
                                stop = false;
                            }
                        }
                    }
                    $('#wait-modal').modal('hide');
                    if(json.winner != 0 || this.moves >= 9){
                        this.finished = true;
                        setTimeout(function(){
                            console.log(scope.moves);
                            if(json.winner != 0){
                                if(json.winner == scope.player){
                                    $('#end-modal-lose').modal();
                                }else{
                                    $('#end-modal-win').modal();
                                }
                            }else if(scope.moves >= 9){   
                                $('#end-modal-draw').modal();
                            }
                        }, 2000)
                    }
                });
            }
        },
        new_game: function(){
            this.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]];
            this.moves = 0;
            this.finished = false;
            $('.modal').each(function(){
                $(this).modal('hide');
            });
        }
    }
});