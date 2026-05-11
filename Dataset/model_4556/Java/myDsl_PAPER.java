





import java.util.List;
import java.util.ArrayList;

public class myDsl_PAPER extends CMD {

    private String paperColour;
    private int sizeX;
    private int sizeY;



    public myDsl_PAPER(
        String paperColour,        int sizeX,        int sizeY    ) {
        super(
        );
        this.paperColour = paperColour;
        this.sizeX = sizeX;
        this.sizeY = sizeY;
    }


    public String getPapercolour() {
        return paperColour;
    }

    public void setPapercolour(String paperColour) {
        this.paperColour = paperColour;
    }
    public int getSizex() {
        return sizeX;
    }

    public void setSizex(int sizeX) {
        this.sizeX = sizeX;
    }
    public int getSizey() {
        return sizeY;
    }

    public void setSizey(int sizeY) {
        this.sizeY = sizeY;
    }


}