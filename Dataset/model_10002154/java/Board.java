





import java.util.List;
import java.util.ArrayList;

public class Board  {

    private int NUM_IMAGES;
    private int all_cells;
    private int MARKED_MINE_CELL;
    private int DRAW_MARK;
    private int mines_left;
    private String field;
    private int MINE_CELL;
    private int CELL_SIZE;
    private int COVERED_MINE_CELL;
    private int DRAW_WRONG_MARK;
    private int N_MINES;
    private None statusbar;
    private int DRAW_MINE;
    private int EMPTY_CELL;
    private int DRAW_COVER;
    private int N_COLS;
    private None timeBar;
    private String img;
    private int COVER_FOR_CELL;
    private int MARK_FOR_CELL;
    private int N_ROWS;
    private boolean inGame;





    private Mines mines;


    public Board(
        int NUM_IMAGES,        int all_cells,        int MARKED_MINE_CELL,        int DRAW_MARK,        int mines_left,        String field,        int MINE_CELL,        int CELL_SIZE,        int COVERED_MINE_CELL,        int DRAW_WRONG_MARK,        int N_MINES,        None statusbar,        int DRAW_MINE,        int EMPTY_CELL,        int DRAW_COVER,        int N_COLS,        None timeBar,        String img,        int COVER_FOR_CELL,        int MARK_FOR_CELL,        int N_ROWS,        boolean inGame    ) {
        this.NUM_IMAGES = NUM_IMAGES;
        this.all_cells = all_cells;
        this.MARKED_MINE_CELL = MARKED_MINE_CELL;
        this.DRAW_MARK = DRAW_MARK;
        this.mines_left = mines_left;
        this.field = field;
        this.MINE_CELL = MINE_CELL;
        this.CELL_SIZE = CELL_SIZE;
        this.COVERED_MINE_CELL = COVERED_MINE_CELL;
        this.DRAW_WRONG_MARK = DRAW_WRONG_MARK;
        this.N_MINES = N_MINES;
        this.statusbar = statusbar;
        this.DRAW_MINE = DRAW_MINE;
        this.EMPTY_CELL = EMPTY_CELL;
        this.DRAW_COVER = DRAW_COVER;
        this.N_COLS = N_COLS;
        this.timeBar = timeBar;
        this.img = img;
        this.COVER_FOR_CELL = COVER_FOR_CELL;
        this.MARK_FOR_CELL = MARK_FOR_CELL;
        this.N_ROWS = N_ROWS;
        this.inGame = inGame;
    }


    public int getNum_images() {
        return NUM_IMAGES;
    }

    public void setNum_images(int NUM_IMAGES) {
        this.NUM_IMAGES = NUM_IMAGES;
    }
    public int getAll_cells() {
        return all_cells;
    }

    public void setAll_cells(int all_cells) {
        this.all_cells = all_cells;
    }
    public int getMarked_mine_cell() {
        return MARKED_MINE_CELL;
    }

    public void setMarked_mine_cell(int MARKED_MINE_CELL) {
        this.MARKED_MINE_CELL = MARKED_MINE_CELL;
    }
    public int getDraw_mark() {
        return DRAW_MARK;
    }

    public void setDraw_mark(int DRAW_MARK) {
        this.DRAW_MARK = DRAW_MARK;
    }
    public int getMines_left() {
        return mines_left;
    }

    public void setMines_left(int mines_left) {
        this.mines_left = mines_left;
    }
    public String getField() {
        return field;
    }

    public void setField(String field) {
        this.field = field;
    }
    public int getMine_cell() {
        return MINE_CELL;
    }

    public void setMine_cell(int MINE_CELL) {
        this.MINE_CELL = MINE_CELL;
    }
    public int getCell_size() {
        return CELL_SIZE;
    }

    public void setCell_size(int CELL_SIZE) {
        this.CELL_SIZE = CELL_SIZE;
    }
    public int getCovered_mine_cell() {
        return COVERED_MINE_CELL;
    }

    public void setCovered_mine_cell(int COVERED_MINE_CELL) {
        this.COVERED_MINE_CELL = COVERED_MINE_CELL;
    }
    public int getDraw_wrong_mark() {
        return DRAW_WRONG_MARK;
    }

    public void setDraw_wrong_mark(int DRAW_WRONG_MARK) {
        this.DRAW_WRONG_MARK = DRAW_WRONG_MARK;
    }
    public int getN_mines() {
        return N_MINES;
    }

    public void setN_mines(int N_MINES) {
        this.N_MINES = N_MINES;
    }
    public None getStatusbar() {
        return statusbar;
    }

    public void setStatusbar(None statusbar) {
        this.statusbar = statusbar;
    }
    public int getDraw_mine() {
        return DRAW_MINE;
    }

    public void setDraw_mine(int DRAW_MINE) {
        this.DRAW_MINE = DRAW_MINE;
    }
    public int getEmpty_cell() {
        return EMPTY_CELL;
    }

    public void setEmpty_cell(int EMPTY_CELL) {
        this.EMPTY_CELL = EMPTY_CELL;
    }
    public int getDraw_cover() {
        return DRAW_COVER;
    }

    public void setDraw_cover(int DRAW_COVER) {
        this.DRAW_COVER = DRAW_COVER;
    }
    public int getN_cols() {
        return N_COLS;
    }

    public void setN_cols(int N_COLS) {
        this.N_COLS = N_COLS;
    }
    public None getTimebar() {
        return timeBar;
    }

    public void setTimebar(None timeBar) {
        this.timeBar = timeBar;
    }
    public String getImg() {
        return img;
    }

    public void setImg(String img) {
        this.img = img;
    }
    public int getCover_for_cell() {
        return COVER_FOR_CELL;
    }

    public void setCover_for_cell(int COVER_FOR_CELL) {
        this.COVER_FOR_CELL = COVER_FOR_CELL;
    }
    public int getMark_for_cell() {
        return MARK_FOR_CELL;
    }

    public void setMark_for_cell(int MARK_FOR_CELL) {
        this.MARK_FOR_CELL = MARK_FOR_CELL;
    }
    public int getN_rows() {
        return N_ROWS;
    }

    public void setN_rows(int N_ROWS) {
        this.N_ROWS = N_ROWS;
    }
    public boolean getIngame() {
        return inGame;
    }

    public void setIngame(boolean inGame) {
        this.inGame = inGame;
    }

    public Mines getMines() {
        return mines;
    }

    public void setMines(Mines mines) {
        this.mines = mines;
    }

}