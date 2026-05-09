





import java.util.List;
import java.util.ArrayList;

public class uma_Tool extends ContentCategory {






    private List<uma_ToolMentor> uma_toolmentors;


    public uma_Tool(
    ) {
        super(
        );
        this.uma_toolmentors = new ArrayList<>();
    }

    public uma_Tool(
        ArrayList<uma_ToolMentor> uma_toolmentors    ) {
        this.uma_toolmentors = uma_toolmentors;
    }


    public List<uma_ToolMentor> getUma_toolmentors() {
        return uma_toolmentors;
    }

    public void addUma_toolmentor(Uma_toolmentor uma_toolmentor) {
        this.uma_toolmentors.add(uma_toolmentor);
    }

}