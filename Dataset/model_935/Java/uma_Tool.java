





import java.util.List;
import java.util.ArrayList;

public class uma_Tool extends ContentCategory {

    private String group2;
    private String toolMentor;



    public uma_Tool(
        String group2,        String toolMentor    ) {
        super(
        );
        this.group2 = group2;
        this.toolMentor = toolMentor;
    }


    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }
    public String getToolmentor() {
        return toolMentor;
    }

    public void setToolmentor(String toolMentor) {
        this.toolMentor = toolMentor;
    }


}