





import java.util.List;
import java.util.ArrayList;

public class model_FontProperties extends Feature {

    private int size;
    private boolean italics;
    private String face;
    private boolean bold;



    public model_FontProperties(
        int size,        boolean italics,        String face,        boolean bold    ) {
        super(
        );
        this.size = size;
        this.italics = italics;
        this.face = face;
        this.bold = bold;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public boolean getItalics() {
        return italics;
    }

    public void setItalics(boolean italics) {
        this.italics = italics;
    }
    public String getFace() {
        return face;
    }

    public void setFace(String face) {
        this.face = face;
    }
    public boolean getBold() {
        return bold;
    }

    public void setBold(boolean bold) {
        this.bold = bold;
    }


}