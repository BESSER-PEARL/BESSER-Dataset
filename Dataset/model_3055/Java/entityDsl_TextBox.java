





import java.util.List;
import java.util.ArrayList;

public class entityDsl_TextBox  {

    private int maxTextLength;
    private String name;
    private int minTextLength;



    public entityDsl_TextBox(
        int maxTextLength,        String name,        int minTextLength    ) {
        this.maxTextLength = maxTextLength;
        this.name = name;
        this.minTextLength = minTextLength;
    }


    public int getMaxtextlength() {
        return maxTextLength;
    }

    public void setMaxtextlength(int maxTextLength) {
        this.maxTextLength = maxTextLength;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getMintextlength() {
        return minTextLength;
    }

    public void setMintextlength(int minTextLength) {
        this.minTextLength = minTextLength;
    }


}