





import java.util.List;
import java.util.ArrayList;

public class classLayout2Frontend_PageView  {

    private String name;
    private String layoutType;



    public classLayout2Frontend_PageView(
        String name,        String layoutType    ) {
        this.name = name;
        this.layoutType = layoutType;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLayouttype() {
        return layoutType;
    }

    public void setLayouttype(String layoutType) {
        this.layoutType = layoutType;
    }


}