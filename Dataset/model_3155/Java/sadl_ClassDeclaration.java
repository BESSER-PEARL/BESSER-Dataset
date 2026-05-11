





import java.util.List;
import java.util.ArrayList;

public class sadl_ClassDeclaration extends Statement {






    private sadl_EnumeratedInstances sadl_enumeratedinstances;




    private sadl_ResourceName sadl_resourcename;




    private List<sadl_AddlClassInfo> sadl_addlclassinfos;




    private sadl_ResourceIdentifier sadl_resourceidentifier;




    private sadl_ResourceList sadl_resourcelist;


    public sadl_ClassDeclaration(
    ) {
        super(
        );
        this.sadl_addlclassinfos = new ArrayList<>();
    }

    public sadl_ClassDeclaration(
        ArrayList<sadl_AddlClassInfo> sadl_addlclassinfos    ) {
        this.sadl_addlclassinfos = sadl_addlclassinfos;
    }


    public sadl_EnumeratedInstances getSadl_enumeratedinstances() {
        return sadl_enumeratedinstances;
    }

    public void setSadl_enumeratedinstances(sadl_EnumeratedInstances sadl_enumeratedinstances) {
        this.sadl_enumeratedinstances = sadl_enumeratedinstances;
    }
    public sadl_ResourceName getSadl_resourcename() {
        return sadl_resourcename;
    }

    public void setSadl_resourcename(sadl_ResourceName sadl_resourcename) {
        this.sadl_resourcename = sadl_resourcename;
    }
    public List<sadl_AddlClassInfo> getSadl_addlclassinfos() {
        return sadl_addlclassinfos;
    }

    public void addSadl_addlclassinfo(Sadl_addlclassinfo sadl_addlclassinfo) {
        this.sadl_addlclassinfos.add(sadl_addlclassinfo);
    }
    public sadl_ResourceIdentifier getSadl_resourceidentifier() {
        return sadl_resourceidentifier;
    }

    public void setSadl_resourceidentifier(sadl_ResourceIdentifier sadl_resourceidentifier) {
        this.sadl_resourceidentifier = sadl_resourceidentifier;
    }
    public sadl_ResourceList getSadl_resourcelist() {
        return sadl_resourcelist;
    }

    public void setSadl_resourcelist(sadl_ResourceList sadl_resourcelist) {
        this.sadl_resourcelist = sadl_resourcelist;
    }

}