





import java.util.List;
import java.util.ArrayList;

public class easyflow_Library extends GroupingCriterion {

    private String name;
    private int readLength;
    private int insertSize;



    public easyflow_Library(
        String name,        int readLength,        int insertSize    ) {
        super(
        );
        this.name = name;
        this.readLength = readLength;
        this.insertSize = insertSize;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getReadlength() {
        return readLength;
    }

    public void setReadlength(int readLength) {
        this.readLength = readLength;
    }
    public int getInsertsize() {
        return insertSize;
    }

    public void setInsertsize(int insertSize) {
        this.insertSize = insertSize;
    }


}