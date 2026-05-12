





import java.util.List;
import java.util.ArrayList;

public class Connect4_connect  {

    private int x;
    private int columnSize;
    private int y;
    private int FRAME_HEIGHT;
    private String label3;
    private int FRAME_WIDTH;
    private String label1;
    private String panel;
    private String label5;
    private String label4;
    private int rowSize;
    private String label2;



    public Connect4_connect(
        int x,        int columnSize,        int y,        int FRAME_HEIGHT,        String label3,        int FRAME_WIDTH,        String label1,        String panel,        String label5,        String label4,        int rowSize,        String label2    ) {
        this.x = x;
        this.columnSize = columnSize;
        this.y = y;
        this.FRAME_HEIGHT = FRAME_HEIGHT;
        this.label3 = label3;
        this.FRAME_WIDTH = FRAME_WIDTH;
        this.label1 = label1;
        this.panel = panel;
        this.label5 = label5;
        this.label4 = label4;
        this.rowSize = rowSize;
        this.label2 = label2;
    }


    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getColumnsize() {
        return columnSize;
    }

    public void setColumnsize(int columnSize) {
        this.columnSize = columnSize;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public int getFrame_height() {
        return FRAME_HEIGHT;
    }

    public void setFrame_height(int FRAME_HEIGHT) {
        this.FRAME_HEIGHT = FRAME_HEIGHT;
    }
    public String getLabel3() {
        return label3;
    }

    public void setLabel3(String label3) {
        this.label3 = label3;
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
    public String getPanel() {
        return panel;
    }

    public void setPanel(String panel) {
        this.panel = panel;
    }
    public String getLabel5() {
        return label5;
    }

    public void setLabel5(String label5) {
        this.label5 = label5;
    }
    public String getLabel4() {
        return label4;
    }

    public void setLabel4(String label4) {
        this.label4 = label4;
    }
    public int getRowsize() {
        return rowSize;
    }

    public void setRowsize(int rowSize) {
        this.rowSize = rowSize;
    }
    public String getLabel2() {
        return label2;
    }

    public void setLabel2(String label2) {
        this.label2 = label2;
    }


}