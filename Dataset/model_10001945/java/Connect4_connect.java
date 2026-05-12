





import java.util.List;
import java.util.ArrayList;

public class Connect4_connect  {

    private int FRAME_HEIGHT;
    private int rowSize;
    private int x;
    private String label4;
    private String panel;
    private int FRAME_WIDTH;
    private String label1;
    private String label5;
    private String label3;
    private int y;
    private String label2;
    private int columnSize;





    private Connect4_Board connect4_board;




    private Connect4_CirclePanel connect4_circlepanel;


    public Connect4_connect(
        int FRAME_HEIGHT,        int rowSize,        int x,        String label4,        String panel,        int FRAME_WIDTH,        String label1,        String label5,        String label3,        int y,        String label2,        int columnSize    ) {
        this.FRAME_HEIGHT = FRAME_HEIGHT;
        this.rowSize = rowSize;
        this.x = x;
        this.label4 = label4;
        this.panel = panel;
        this.FRAME_WIDTH = FRAME_WIDTH;
        this.label1 = label1;
        this.label5 = label5;
        this.label3 = label3;
        this.y = y;
        this.label2 = label2;
        this.columnSize = columnSize;
    }


    public int getFrame_height() {
        return FRAME_HEIGHT;
    }

    public void setFrame_height(int FRAME_HEIGHT) {
        this.FRAME_HEIGHT = FRAME_HEIGHT;
    }
    public int getRowsize() {
        return rowSize;
    }

    public void setRowsize(int rowSize) {
        this.rowSize = rowSize;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public String getLabel4() {
        return label4;
    }

    public void setLabel4(String label4) {
        this.label4 = label4;
    }
    public String getPanel() {
        return panel;
    }

    public void setPanel(String panel) {
        this.panel = panel;
    }
    public int getFrame_width() {
        return FRAME_WIDTH;
    }

    public void setFrame_width(int FRAME_WIDTH) {
        this.FRAME_WIDTH = FRAME_WIDTH;
    }
    public String getLabel1() {
        return label1;
    }

    public void setLabel1(String label1) {
        this.label1 = label1;
    }
    public String getLabel5() {
        return label5;
    }

    public void setLabel5(String label5) {
        this.label5 = label5;
    }
    public String getLabel3() {
        return label3;
    }

    public void setLabel3(String label3) {
        this.label3 = label3;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public String getLabel2() {
        return label2;
    }

    public void setLabel2(String label2) {
        this.label2 = label2;
    }
    public int getColumnsize() {
        return columnSize;
    }

    public void setColumnsize(int columnSize) {
        this.columnSize = columnSize;
    }

    public Connect4_Board getConnect4_board() {
        return connect4_board;
    }

    public void setConnect4_board(Connect4_Board connect4_board) {
        this.connect4_board = connect4_board;
    }
    public Connect4_CirclePanel getConnect4_circlepanel() {
        return connect4_circlepanel;
    }

    public void setConnect4_circlepanel(Connect4_CirclePanel connect4_circlepanel) {
        this.connect4_circlepanel = connect4_circlepanel;
    }

}