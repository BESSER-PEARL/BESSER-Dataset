





import java.util.List;
import java.util.ArrayList;

public class eJSL_PageAction  {

    private String pageActionPosition;
    private String name;
    private String pageActionType;



    public eJSL_PageAction(
        String pageActionPosition,        String name,        String pageActionType    ) {
        this.pageActionPosition = pageActionPosition;
        this.name = name;
        this.pageActionType = pageActionType;
    }


    public String getPageactionposition() {
        return pageActionPosition;
    }

    public void setPageactionposition(String pageActionPosition) {
        this.pageActionPosition = pageActionPosition;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPageactiontype() {
        return pageActionType;
    }

    public void setPageactiontype(String pageActionType) {
        this.pageActionType = pageActionType;
    }


}