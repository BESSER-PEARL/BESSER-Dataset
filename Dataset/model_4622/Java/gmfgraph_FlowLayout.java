





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FlowLayout extends Layout {

    private boolean vertical;
    private int minorSpacing;
    private String majorAlignment;
    private boolean forceSingleLine;
    private String minorAlignment;
    private int majorSpacing;
    private boolean matchMinorSize;



    public gmfgraph_FlowLayout(
        boolean vertical,        int minorSpacing,        String majorAlignment,        boolean forceSingleLine,        String minorAlignment,        int majorSpacing,        boolean matchMinorSize    ) {
        super(
        );
        this.vertical = vertical;
        this.minorSpacing = minorSpacing;
        this.majorAlignment = majorAlignment;
        this.forceSingleLine = forceSingleLine;
        this.minorAlignment = minorAlignment;
        this.majorSpacing = majorSpacing;
        this.matchMinorSize = matchMinorSize;
    }


    public boolean getVertical() {
        return vertical;
    }

    public void setVertical(boolean vertical) {
        this.vertical = vertical;
    }
    public int getMinorspacing() {
        return minorSpacing;
    }

    public void setMinorspacing(int minorSpacing) {
        this.minorSpacing = minorSpacing;
    }
    public String getMajoralignment() {
        return majorAlignment;
    }

    public void setMajoralignment(String majorAlignment) {
        this.majorAlignment = majorAlignment;
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
    public int getMajorspacing() {
        return majorSpacing;
    }

    public void setMajorspacing(int majorSpacing) {
        this.majorSpacing = majorSpacing;
    }
    public boolean getMatchminorsize() {
        return matchMinorSize;
    }

    public void setMatchminorsize(boolean matchMinorSize) {
        this.matchMinorSize = matchMinorSize;
    }


}