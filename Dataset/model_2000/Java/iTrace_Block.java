





import java.util.List;
import java.util.ArrayList;

public class iTrace_Block  {

    private int startColumn;
    private int blockNumber;
    private int endLine;
    private int endColumn;
    private int startLine;





    private iTrace_M2TLink itrace_m2tlink;




    private iTrace_M2TLink itrace_m2tlink;


    public iTrace_Block(
        int startColumn,        int blockNumber,        int endLine,        int endColumn,        int startLine    ) {
        this.startColumn = startColumn;
        this.blockNumber = blockNumber;
        this.endLine = endLine;
        this.endColumn = endColumn;
        this.startLine = startLine;
    }


    public int getStartcolumn() {
        return startColumn;
    }

    public void setStartcolumn(int startColumn) {
        this.startColumn = startColumn;
    }
    public int getBlocknumber() {
        return blockNumber;
    }

    public void setBlocknumber(int blockNumber) {
        this.blockNumber = blockNumber;
    }
    public int getEndline() {
        return endLine;
    }

    public void setEndline(int endLine) {
        this.endLine = endLine;
    }
    public int getEndcolumn() {
        return endColumn;
    }

    public void setEndcolumn(int endColumn) {
        this.endColumn = endColumn;
    }
    public int getStartline() {
        return startLine;
    }

    public void setStartline(int startLine) {
        this.startLine = startLine;
    }

    public iTrace_M2TLink getItrace_m2tlink() {
        return itrace_m2tlink;
    }

    public void setItrace_m2tlink(iTrace_M2TLink itrace_m2tlink) {
        this.itrace_m2tlink = itrace_m2tlink;
    }
    public iTrace_M2TLink getItrace_m2tlink() {
        return itrace_m2tlink;
    }

    public void setItrace_m2tlink(iTrace_M2TLink itrace_m2tlink) {
        this.itrace_m2tlink = itrace_m2tlink;
    }

}