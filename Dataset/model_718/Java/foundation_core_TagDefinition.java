





import java.util.List;
import java.util.ArrayList;

public class foundation_core_TagDefinition extends ModelElement {

    private String tagType;



    public foundation_core_TagDefinition(
        String tagType    ) {
        super(
        );
        this.tagType = tagType;
    }


    public String getTagtype() {
        return tagType;
    }

    public void setTagtype(String tagType) {
        this.tagType = tagType;
    }


}