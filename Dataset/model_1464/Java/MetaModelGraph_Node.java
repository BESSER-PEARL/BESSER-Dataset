





import java.util.List;
import java.util.ArrayList;

public class MetaModelGraph_Node  {

    private String extension;
    private String icon;
    private String enumModularNotation;
    private boolean insideRecursion;





    private MetaModelGraph_EClass metamodelgraph_eclass;




    private MetaModelGraph_Composition metamodelgraph_composition;




    private List<MetaModelGraph_Reference> metamodelgraph_references;




    private MetaModelGraph_Node metamodelgraph_node;




    private MetaModelGraph_SubGraph metamodelgraph_subgraph;




    private MetaModelGraph_SubGraph metamodelgraph_subgraph;




    private List<MetaModelGraph_SubClass> metamodelgraph_subclasss;




    private List<MetaModelGraph_Composition> metamodelgraph_compositions;




    private List<MetaModelGraph_SubClass> metamodelgraph_subclasss;




    private List<MetaModelGraph_Composition> metamodelgraph_compositions;


    public MetaModelGraph_Node(
        String extension,        String icon,        String enumModularNotation,        boolean insideRecursion    ) {
        this.extension = extension;
        this.icon = icon;
        this.enumModularNotation = enumModularNotation;
        this.insideRecursion = insideRecursion;
        this.metamodelgraph_references = new ArrayList<>();
        this.metamodelgraph_subclasss = new ArrayList<>();
        this.metamodelgraph_compositions = new ArrayList<>();
        this.metamodelgraph_subclasss = new ArrayList<>();
        this.metamodelgraph_compositions = new ArrayList<>();
    }

    public MetaModelGraph_Node(
        String extension,        String icon,        String enumModularNotation,        boolean insideRecursion        ArrayList<MetaModelGraph_Reference> metamodelgraph_references,        ArrayList<MetaModelGraph_SubClass> metamodelgraph_subclasss,        ArrayList<MetaModelGraph_Composition> metamodelgraph_compositions,        ArrayList<MetaModelGraph_SubClass> metamodelgraph_subclasss,        ArrayList<MetaModelGraph_Composition> metamodelgraph_compositions    ) {
        this.extension = extension;
        this.icon = icon;
        this.enumModularNotation = enumModularNotation;
        this.insideRecursion = insideRecursion;
        this.metamodelgraph_references = metamodelgraph_references;
        this.metamodelgraph_subclasss = metamodelgraph_subclasss;
        this.metamodelgraph_compositions = metamodelgraph_compositions;
        this.metamodelgraph_subclasss = metamodelgraph_subclasss;
        this.metamodelgraph_compositions = metamodelgraph_compositions;
    }

    public String getExtension() {
        return extension;
    }

    public void setExtension(String extension) {
        this.extension = extension;
    }
    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public String getEnummodularnotation() {
        return enumModularNotation;
    }

    public void setEnummodularnotation(String enumModularNotation) {
        this.enumModularNotation = enumModularNotation;
    }
    public boolean getInsiderecursion() {
        return insideRecursion;
    }

    public void setInsiderecursion(boolean insideRecursion) {
        this.insideRecursion = insideRecursion;
    }

    public MetaModelGraph_EClass getMetamodelgraph_eclass() {
        return metamodelgraph_eclass;
    }

    public void setMetamodelgraph_eclass(MetaModelGraph_EClass metamodelgraph_eclass) {
        this.metamodelgraph_eclass = metamodelgraph_eclass;
    }
    public MetaModelGraph_Composition getMetamodelgraph_composition() {
        return metamodelgraph_composition;
    }

    public void setMetamodelgraph_composition(MetaModelGraph_Composition metamodelgraph_composition) {
        this.metamodelgraph_composition = metamodelgraph_composition;
    }
    public List<MetaModelGraph_Reference> getMetamodelgraph_references() {
        return metamodelgraph_references;
    }

    public void addMetamodelgraph_reference(Metamodelgraph_reference metamodelgraph_reference) {
        this.metamodelgraph_references.add(metamodelgraph_reference);
    }
    public MetaModelGraph_Node getMetamodelgraph_node() {
        return metamodelgraph_node;
    }

    public void setMetamodelgraph_node(MetaModelGraph_Node metamodelgraph_node) {
        this.metamodelgraph_node = metamodelgraph_node;
    }
    public MetaModelGraph_SubGraph getMetamodelgraph_subgraph() {
        return metamodelgraph_subgraph;
    }

    public void setMetamodelgraph_subgraph(MetaModelGraph_SubGraph metamodelgraph_subgraph) {
        this.metamodelgraph_subgraph = metamodelgraph_subgraph;
    }
    public MetaModelGraph_SubGraph getMetamodelgraph_subgraph() {
        return metamodelgraph_subgraph;
    }

    public void setMetamodelgraph_subgraph(MetaModelGraph_SubGraph metamodelgraph_subgraph) {
        this.metamodelgraph_subgraph = metamodelgraph_subgraph;
    }
    public List<MetaModelGraph_SubClass> getMetamodelgraph_subclasss() {
        return metamodelgraph_subclasss;
    }

    public void addMetamodelgraph_subclass(Metamodelgraph_subclass metamodelgraph_subclass) {
        this.metamodelgraph_subclasss.add(metamodelgraph_subclass);
    }
    public List<MetaModelGraph_Composition> getMetamodelgraph_compositions() {
        return metamodelgraph_compositions;
    }

    public void addMetamodelgraph_composition(Metamodelgraph_composition metamodelgraph_composition) {
        this.metamodelgraph_compositions.add(metamodelgraph_composition);
    }
    public List<MetaModelGraph_SubClass> getMetamodelgraph_subclasss() {
        return metamodelgraph_subclasss;
    }

    public void addMetamodelgraph_subclass(Metamodelgraph_subclass metamodelgraph_subclass) {
        this.metamodelgraph_subclasss.add(metamodelgraph_subclass);
    }
    public List<MetaModelGraph_Composition> getMetamodelgraph_compositions() {
        return metamodelgraph_compositions;
    }

    public void addMetamodelgraph_composition(Metamodelgraph_composition metamodelgraph_composition) {
        this.metamodelgraph_compositions.add(metamodelgraph_composition);
    }

}