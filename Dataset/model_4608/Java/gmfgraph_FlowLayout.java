





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FlowLayout extends Layout {

    private boolean matchMinorSize;
    private int minorSpacing;
    private boolean forceSingleLine;
    private String minorAlignment;
    private String majorAlignment;
    private boolean vertical;
    private int majorSpacing;



    public gmfgraph_FlowLayout(
        boolean matchMinorSize,        int minorSpacing,        boolean forceSingleLine,        String minorAlignment,        String majorAlignment,        boolean vertical,        int majorSpacing    ) {
        super(
        );
        this.matchMinorSize = matchMinorSize;
        this.minorSpacing = minorSpacing;
        this.forceSingleLine = forceSingleLine;
        this.minorAlignment = minorAlignment;
        this.majorAlignment = majorAlignment;
        this.vertical = vertical;
        this.majorSpacing = majorSpacing;
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
    public boolean getVertical() {
        return vertical;
    }

    public void setVertical(boolean vertical) {
        this.vertical = vertical;
    }
    public int getMajorspacing() {
        return majorSpacing;
    }

    public void setMajorspacing(int majorSpacing) {
        this.majorSpacing = majorSpacing;
    }


}