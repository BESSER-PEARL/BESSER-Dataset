





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FlowLayout extends Layout {

    private int minorSpacing;
    private int majorSpacing;
    private boolean forceSingleLine;
    private boolean matchMinorSize;
    private boolean vertical;
    private String majorAlignment;
    private String minorAlignment;



    public gmfgraph_FlowLayout(
        int minorSpacing,        int majorSpacing,        boolean forceSingleLine,        boolean matchMinorSize,        boolean vertical,        String majorAlignment,        String minorAlignment    ) {
        super(
        );
        this.minorSpacing = minorSpacing;
        this.majorSpacing = majorSpacing;
        this.forceSingleLine = forceSingleLine;
        this.matchMinorSize = matchMinorSize;
        this.vertical = vertical;
        this.majorAlignment = majorAlignment;
        this.minorAlignment = minorAlignment;
    }


    public int getMinorspacing() {
        return minorSpacing;
    }

    public void setMinorspacing(int minorSpacing) {
        this.minorSpacing = minorSpacing;
    }
    public int getMajorspacing() {
        return majorSpacing;
    }

    public void setMajorspacing(int majorSpacing) {
        this.majorSpacing = majorSpacing;
    }
    public boolean getForcesingleline() {
        return forceSingleLine;
    }

    public void setForcesingleline(boolean forceSingleLine) {
        this.forceSingleLine = forceSingleLine;
    }
    public boolean getMatchminorsize() {
        return matchMinorSize;
    }

    public void setMatchminorsize(boolean matchMinorSize) {
        this.matchMinorSize = matchMinorSize;
    }
    public boolean getVertical() {
        return vertical;
    }

    public void setVertical(boolean vertical) {
        this.vertical = vertical;
    }
    public String getMajoralignment() {
        return majorAlignment;
    }

    public void setMajoralignment(String majorAlignment) {
        this.majorAlignment = majorAlignment;
    }
    public String getMinoralignment() {
        return minorAlignment;
    }

    public void setMinoralignment(String minorAlignment) {
        this.minorAlignment = minorAlignment;
    }


}