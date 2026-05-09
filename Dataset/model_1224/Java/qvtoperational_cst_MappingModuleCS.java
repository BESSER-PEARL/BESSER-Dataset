





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_MappingModuleCS extends CSTNode {






    private List<MappingMethodCS> mappingmethodcss;




    private List<ModulePropertyCS> modulepropertycss;




    private List<TagCS> tagcss;




    private List<RenameCS> renamecss;




    private List<ClassifierDefCS> classifierdefcss;


    public qvtoperational_cst_MappingModuleCS(
    ) {
        super(
        );
        this.mappingmethodcss = new ArrayList<>();
        this.modulepropertycss = new ArrayList<>();
        this.tagcss = new ArrayList<>();
        this.renamecss = new ArrayList<>();
        this.classifierdefcss = new ArrayList<>();
    }

    public qvtoperational_cst_MappingModuleCS(
        ArrayList<MappingMethodCS> mappingmethodcss,        ArrayList<ModulePropertyCS> modulepropertycss,        ArrayList<TagCS> tagcss,        ArrayList<RenameCS> renamecss,        ArrayList<ClassifierDefCS> classifierdefcss    ) {
        this.mappingmethodcss = mappingmethodcss;
        this.modulepropertycss = modulepropertycss;
        this.tagcss = tagcss;
        this.renamecss = renamecss;
        this.classifierdefcss = classifierdefcss;
    }


    public List<MappingMethodCS> getMappingmethodcss() {
        return mappingmethodcss;
    }

    public void addMappingmethodcs(Mappingmethodcs mappingmethodcs) {
        this.mappingmethodcss.add(mappingmethodcs);
    }
    public List<ModulePropertyCS> getModulepropertycss() {
        return modulepropertycss;
    }

    public void addModulepropertycs(Modulepropertycs modulepropertycs) {
        this.modulepropertycss.add(modulepropertycs);
    }
    public List<TagCS> getTagcss() {
        return tagcss;
    }

    public void addTagcs(Tagcs tagcs) {
        this.tagcss.add(tagcs);
    }
    public List<RenameCS> getRenamecss() {
        return renamecss;
    }

    public void addRenamecs(Renamecs renamecs) {
        this.renamecss.add(renamecs);
    }
    public List<ClassifierDefCS> getClassifierdefcss() {
        return classifierdefcss;
    }

    public void addClassifierdefcs(Classifierdefcs classifierdefcs) {
        this.classifierdefcss.add(classifierdefcs);
    }

}