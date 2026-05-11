





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FlowLayout extends Layout {

    private boolean vertical;
    private boolean matchMinorSize;
    private int minorSpacing;
    private int majorSpacing;
    private boolean forceSingleLine;
    private String minorAlignment;
    private String majorAlignment;



    public gmfgraph_FlowLayout(
        boolean vertical,        boolean matchMinorSize,        int minorSpacing,        int majorSpacing,        boolean forceSingleLine,        String minorAlignment,        String majorAlignment    ) {
        super(
        );
        this.vertical = vertical;
        this.matchMinorSize = matchMinorSize;
        this.minorSpacing = minorSpacing;
        this.majorSpacing = majorSpacing;
        this.forceSingleLine = forceSingleLine;
        this.minorAlignment = minorAlignment;
        this.majorAlignment = majorAlignment;
    }


    public boolean getVertical() {
        return vertical;
    }

    public void setVertical(boolean vertical) {
        this.vertical = vertical;
    }
    public boolean getMatchminorsize() {
        return matchMinorSize;
    }

    public void setMatchminorsize(boolean matchMinorSize) {
        this.matchMinorSize = matchMinorSize;
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
    public String getMinoralignment() {
        return minorAlignment;
    }

    public void setMinoralignment(String minorAlignment) {
        this.minorAlignment = minorAlignment;
    }
    public String getMajoralignment() {
        return majorAlignment;
    }

    public void setMajoralignment(String majorAlignment) {
        this.majorAlignment = majorAlignment;
    }


}