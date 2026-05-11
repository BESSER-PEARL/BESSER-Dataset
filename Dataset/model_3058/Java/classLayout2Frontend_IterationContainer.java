





import java.util.List;
import java.util.ArrayList;

public class classLayout2Frontend_IterationContainer extends ContainerView {






    private List<classLayout2Frontend_IterationFilter> classlayout2frontend_iterationfilters;


    public classLayout2Frontend_IterationContainer(
    ) {
        super(
        );
        this.classlayout2frontend_iterationfilters = new ArrayList<>();
    }

    public classLayout2Frontend_IterationContainer(
        ArrayList<classLayout2Frontend_IterationFilter> classlayout2frontend_iterationfilters    ) {
        this.classlayout2frontend_iterationfilters = classlayout2frontend_iterationfilters;
    }


    public List<classLayout2Frontend_IterationFilter> getClasslayout2frontend_iterationfilters() {
        return classlayout2frontend_iterationfilters;
    }

    public void addClasslayout2frontend_iterationfilter(Classlayout2frontend_iterationfilter classlayout2frontend_iterationfilter) {
        this.classlayout2frontend_iterationfilters.add(classlayout2frontend_iterationfilter);
    }

}