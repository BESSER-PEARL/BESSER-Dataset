





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FlowLayout extends Layout {

    private int majorSpacing;
    private boolean matchMinorSize;
    private String majorAlignment;
    private boolean vertical;
    private boolean forceSingleLine;
    private String minorAlignment;
    private int minorSpacing;



    public gmfgraph_FlowLayout(
        int majorSpacing,        boolean matchMinorSize,        String majorAlignment,        boolean vertical,        boolean forceSingleLine,        String minorAlignment,        int minorSpacing    ) {
        super(
        );
        this.majorSpacing = majorSpacing;
        this.matchMinorSize = matchMinorSize;
        this.majorAlignment = majorAlignment;
        this.vertical = vertical;
        this.forceSingleLine = forceSingleLine;
        this.minorAlignment = minorAlignment;
        this.minorSpacing = minorSpacing;
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
    public String getMinoralignment() {
        return minorAlignment;
    }

    public void setMinoralignment(String minorAlignment) {
        this.minorAlignment = minorAlignment;
    }
    public int getMinorspacing() {
        return minorSpacing;
    }

    public void setMinorspacing(int minorSpacing) {
        this.minorSpacing = minorSpacing;
    }


}