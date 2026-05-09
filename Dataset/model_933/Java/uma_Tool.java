





import java.util.List;
import java.util.ArrayList;

public class uma_Tool extends ContentCategory {

    private String toolMentor;
    private String group2;



    public uma_Tool(
        String toolMentor,        String group2    ) {
        super(
        );
        this.toolMentor = toolMentor;
        this.group2 = group2;
    }


    public String getToolmentor() {
        return toolMentor;
    }

    public void setToolmentor(String toolMentor) {
        this.toolMentor = toolMentor;
    }
    public String getGroup2() {
        return group2;
    }

    public void setGroup2(String group2) {
        this.group2 = group2;
    }


}