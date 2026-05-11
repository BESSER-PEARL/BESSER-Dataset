





import java.util.List;
import java.util.ArrayList;

public class smalluml_ElementDiagramme  {






    private List<smalluml_TypeDonnee> smalluml_typedonnees;




    private List<smalluml_Association> smalluml_associations;




    private List<smalluml_Classe> smalluml_classes;




    private smalluml_Diagramme smalluml_diagramme;




    private List<smalluml_Enumeration> smalluml_enumerations;


    public smalluml_ElementDiagramme(
    ) {
        this.smalluml_typedonnees = new ArrayList<>();
        this.smalluml_associations = new ArrayList<>();
        this.smalluml_classes = new ArrayList<>();
        this.smalluml_enumerations = new ArrayList<>();
    }

    public smalluml_ElementDiagramme(
        ArrayList<smalluml_TypeDonnee> smalluml_typedonnees,        ArrayList<smalluml_Association> smalluml_associations,        ArrayList<smalluml_Classe> smalluml_classes,        ArrayList<smalluml_Enumeration> smalluml_enumerations    ) {
        this.smalluml_typedonnees = smalluml_typedonnees;
        this.smalluml_associations = smalluml_associations;
        this.smalluml_classes = smalluml_classes;
        this.smalluml_enumerations = smalluml_enumerations;
    }


    public List<smalluml_TypeDonnee> getSmalluml_typedonnees() {
        return smalluml_typedonnees;
    }

    public void addSmalluml_typedonnee(Smalluml_typedonnee smalluml_typedonnee) {
        this.smalluml_typedonnees.add(smalluml_typedonnee);
    }
    public List<smalluml_Association> getSmalluml_associations() {
        return smalluml_associations;
    }

    public void addSmalluml_association(Smalluml_association smalluml_association) {
        this.smalluml_associations.add(smalluml_association);
    }
    public List<smalluml_Classe> getSmalluml_classes() {
        return smalluml_classes;
    }

    public void addSmalluml_classe(Smalluml_classe smalluml_classe) {
        this.smalluml_classes.add(smalluml_classe);
    }
    public smalluml_Diagramme getSmalluml_diagramme() {
        return smalluml_diagramme;
    }

    public void setSmalluml_diagramme(smalluml_Diagramme smalluml_diagramme) {
        this.smalluml_diagramme = smalluml_diagramme;
    }
    public List<smalluml_Enumeration> getSmalluml_enumerations() {
        return smalluml_enumerations;
    }

    public void addSmalluml_enumeration(Smalluml_enumeration smalluml_enumeration) {
        this.smalluml_enumerations.add(smalluml_enumeration);
    }

}