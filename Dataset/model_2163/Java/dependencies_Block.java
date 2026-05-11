





import java.util.List;
import java.util.ArrayList;

public class dependencies_Block  {






    private List<dependencies_CoreClass> dependencies_coreclasss;


    public dependencies_Block(
    ) {
        this.dependencies_coreclasss = new ArrayList<>();
    }

    public dependencies_Block(
        ArrayList<dependencies_CoreClass> dependencies_coreclasss    ) {
        this.dependencies_coreclasss = dependencies_coreclasss;
    }


    public List<dependencies_CoreClass> getDependencies_coreclasss() {
        return dependencies_coreclasss;
    }

    public void addDependencies_coreclass(Dependencies_coreclass dependencies_coreclass) {
        this.dependencies_coreclasss.add(dependencies_coreclass);
    }

}