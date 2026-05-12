





import java.util.List;
import java.util.ArrayList;

public class candyCrushPackage_CandyButton  {

    private int y;
    private int x;
    private String image;
    private String button;





    private ImageIcon_external imageicon_external;




    private candyCrushPackage_Board candycrushpackage_board;




    private JButton_external jbutton_external;


    public candyCrushPackage_CandyButton(
        int y,        int x,        String image,        String button    ) {
        this.y = y;
        this.x = x;
        this.image = image;
        this.button = button;
    }


    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
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
    public String getButton() {
        return button;
    }

    public void setButton(String button) {
        this.button = button;
    }

    public ImageIcon_external getImageicon_external() {
        return imageicon_external;
    }

    public void setImageicon_external(ImageIcon_external imageicon_external) {
        this.imageicon_external = imageicon_external;
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