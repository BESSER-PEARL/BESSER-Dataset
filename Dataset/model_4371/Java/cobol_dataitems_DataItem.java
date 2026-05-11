





import java.util.List;
import java.util.ArrayList;

public class cobol_dataitems_DataItem extends water_IncompleteElement, references_ReferenceableElement {

    private String levelNumber;



    public cobol_dataitems_DataItem(
        String levelNumber    ) {
        super(
        );
        this.levelNumber = levelNumber;
    }


    public String getLevelnumber() {
        return levelNumber;
    }

    public void setLevelnumber(String levelNumber) {
        this.levelNumber = levelNumber;
    }


}