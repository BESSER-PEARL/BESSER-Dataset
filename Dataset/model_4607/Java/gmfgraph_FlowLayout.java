





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FlowLayout extends Layout {

    private String majorAlignment;
    private boolean vertical;
    private boolean forceSingleLine;
    private int minorSpacing;
    private String minorAlignment;
    private boolean matchMinorSize;
    private int majorSpacing;



    public gmfgraph_FlowLayout(
        String majorAlignment,        boolean vertical,        boolean forceSingleLine,        int minorSpacing,        String minorAlignment,        boolean matchMinorSize,        int majorSpacing    ) {
        super(
        );
        this.majorAlignment = majorAlignment;
        this.vertical = vertical;
        this.forceSingleLine = forceSingleLine;
        this.minorSpacing = minorSpacing;
        this.minorAlignment = minorAlignment;
        this.matchMinorSize = matchMinorSize;
        this.majorSpacing = majorSpacing;
    }


    public String getMajoralignment() {
        return majorAlignment;
    }

    public void setMajoralignment(String majorAlignment) {
        this.majorAlignment = majorAlignment;
    }
    public boolean getVertical() {
        return vertical;
    }

    public void setVertical(boolean vertical) {
        this.vertical = vertical;
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
    public int getMajorspacing() {
        return majorSpacing;
    }

    public void setMajorspacing(int majorSpacing) {
        this.majorSpacing = majorSpacing;
    }


}