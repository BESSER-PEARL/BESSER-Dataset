





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_FlowLayout extends Layout {

    private boolean matchMinorSize;
    private int majorSpacing;
    private boolean forceSingleLine;
    private String majorAlignment;
    private boolean vertical;
    private String minorAlignment;
    private int minorSpacing;



    public gmfgraph_FlowLayout(
        boolean matchMinorSize,        int majorSpacing,        boolean forceSingleLine,        String majorAlignment,        boolean vertical,        String minorAlignment,        int minorSpacing    ) {
        super(
        );
        this.matchMinorSize = matchMinorSize;
        this.majorSpacing = majorSpacing;
        this.forceSingleLine = forceSingleLine;
        this.majorAlignment = majorAlignment;
        this.vertical = vertical;
        this.minorAlignment = minorAlignment;
        this.minorSpacing = minorSpacing;
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