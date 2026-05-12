





import java.util.List;
import java.util.ArrayList;

public class candyCrushPackage_CandyButton  {

    private String button;
    private int x;
    private String image;
    private int y;





    private candyCrushPackage_Board candycrushpackage_board;




    private JButton_external jbutton_external;


    public candyCrushPackage_CandyButton(
        String button,        int x,        String image,        int y    ) {
        this.button = button;
        this.x = x;
        this.image = image;
        this.y = y;
    }


    public String getButton() {
        return button;
    }

    public void setButton(String button) {
        this.button = button;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }

    public candyCrushPackage_Board getCandycrushpackage_board() {
        return candycrushpackage_board;
    }

    public void setCandycrushpackage_board(candyCrushPackage_Board candycrushpackage_board) {
        this.candycrushpackage_board = candycrushpackage_board;
    }
    public JButton_external getJbutton_external() {
        return jbutton_external;
    }

    public void setJbutton_external(JButton_external jbutton_external) {
        this.jbutton_external = jbutton_external;
    }

}