





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FlowLayout extends Layout {

    private boolean forceSingleLine;
    private int minorSpacing;
    private boolean vertical;
    private String minorAlignment;
    private boolean matchMinorSize;
    private String majorAlignment;
    private int majorSpacing;



    public gmfgraph_FlowLayout(
        boolean forceSingleLine,        int minorSpacing,        boolean vertical,        String minorAlignment,        boolean matchMinorSize,        String majorAlignment,        int majorSpacing    ) {
        super(
        );
        this.forceSingleLine = forceSingleLine;
        this.minorSpacing = minorSpacing;
        this.vertical = vertical;
        this.minorAlignment = minorAlignment;
        this.matchMinorSize = matchMinorSize;
        this.majorAlignment = majorAlignment;
        this.majorSpacing = majorSpacing;
    }


    public boolean getForcesingleline() {
        return forceSingleLine;
    }

    public void setForcesingleline(boolean forceSingleLine) {
        this.forceSingleLine = forceSingleLine;
    }
    public int getMinorspacing() {
        return minorSpacing;
    }

    public void setMinorspacing(int minorSpacing) {
        this.minorSpacing = minorSpacing;
    }
    public boolean getVertical() {
        return vertical;
    }

    public void setVertical(boolean vertical) {
        this.vertical = vertical;
    }
    public String getMinoralignment() {
        return minorAlignment;
    }

    public void setMinoralignment(String minorAlignment) {
        this.minorAlignment = minorAlignment;
    }
    public boolean getMatchminorsize() {
        return matchMinorSize;
    }

    public void setMatchminorsize(boolean matchMinorSize) {
        this.matchMinorSize = matchMinorSize;
    }
    public String getMajoralignment() {
        return majorAlignment;
    }

    public void setMajoralignment(String majorAlignment) {
        this.majorAlignment = majorAlignment;
    }
    public int getMajorspacing() {
        return majorSpacing;
    }

    public void setMajorspacing(int majorSpacing) {
        this.majorSpacing = majorSpacing;
    }


}