





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FlowLayout extends Layout {

    private boolean matchMinorSize;
    private String minorAlignment;
    private boolean forceSingleLine;
    private String majorAlignment;
    private boolean vertical;
    private int minorSpacing;
    private int majorSpacing;



    public gmfgraph_FlowLayout(
        boolean matchMinorSize,        String minorAlignment,        boolean forceSingleLine,        String majorAlignment,        boolean vertical,        int minorSpacing,        int majorSpacing    ) {
        super(
        );
        this.matchMinorSize = matchMinorSize;
        this.minorAlignment = minorAlignment;
        this.forceSingleLine = forceSingleLine;
        this.majorAlignment = majorAlignment;
        this.vertical = vertical;
        this.minorSpacing = minorSpacing;
        this.majorSpacing = majorSpacing;
    }


    public boolean getMatchminorsize() {
        return matchMinorSize;
    }

    public void setMatchminorsize(boolean matchMinorSize) {
        this.matchMinorSize = matchMinorSize;
    }
    public String getMinoralignment() {
        return minorAlignment;
    }

    public void setMinoralignment(String minorAlignment) {
        this.minorAlignment = minorAlignment;
    }
    public boolean getForcesingleline() {
        return forceSingleLine;
    }

    public void setForcesingleline(boolean forceSingleLine) {
        this.forceSingleLine = forceSingleLine;
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


}