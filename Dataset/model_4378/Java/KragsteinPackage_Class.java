





import java.util.List;
import java.util.ArrayList;

public class KragsteinPackage_Class extends Unit {

    private String visibility;
    private String supplierElement;
    private boolean isSingletone;
    private String name;
    private boolean isInterface;
    private String superClass;





    private KragsteinPackage_Relationship kragsteinpackage_relationship;




    private List<KragsteinPackage_Relationship> kragsteinpackage_relationships;




    private KragsteinPackage_Relationship kragsteinpackage_relationship;


    public KragsteinPackage_Class(
        String visibility,        String supplierElement,        boolean isSingletone,        String name,        boolean isInterface,        String superClass    ) {
        super(
        );
        this.visibility = visibility;
        this.supplierElement = supplierElement;
        this.isSingletone = isSingletone;
        this.name = name;
        this.isInterface = isInterface;
        this.superClass = superClass;
        this.kragsteinpackage_relationships = new ArrayList<>();
    }

    public KragsteinPackage_Class(
        String visibility,        String supplierElement,        boolean isSingletone,        String name,        boolean isInterface,        String superClass        ArrayList<KragsteinPackage_Relationship> kragsteinpackage_relationships    ) {
        this.visibility = visibility;
        this.supplierElement = supplierElement;
        this.isSingletone = isSingletone;
        this.name = name;
        this.isInterface = isInterface;
        this.superClass = superClass;
        this.kragsteinpackage_relationships = kragsteinpackage_relationships;
    }

    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getSupplierelement() {
        return supplierElement;
    }

    public void setSupplierelement(String supplierElement) {
        this.supplierElement = supplierElement;
    }
    public boolean getIssingletone() {
        return isSingletone;
    }

    public void setIssingletone(boolean isSingletone) {
        this.isSingletone = isSingletone;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsinterface() {
        return isInterface;
    }

    public void setIsinterface(boolean isInterface) {
        this.isInterface = isInterface;
    }
    public String getSuperclass() {
        return superClass;
    }

    public void setSuperclass(String superClass) {
        this.superClass = superClass;
    }

    public KragsteinPackage_Relationship getKragsteinpackage_relationship() {
        return kragsteinpackage_relationship;
    }

    public void setKragsteinpackage_relationship(KragsteinPackage_Relationship kragsteinpackage_relationship) {
        this.kragsteinpackage_relationship = kragsteinpackage_relationship;
    }
    public List<KragsteinPackage_Relationship> getKragsteinpackage_relationships() {
        return kragsteinpackage_relationships;
    }

    public void addKragsteinpackage_relationship(Kragsteinpackage_relationship kragsteinpackage_relationship) {
        this.kragsteinpackage_relationships.add(kragsteinpackage_relationship);
    }
    public KragsteinPackage_Relationship getKragsteinpackage_relationship() {
        return kragsteinpackage_relationship;
    }

    public void setKragsteinpackage_relationship(KragsteinPackage_Relationship kragsteinpackage_relationship) {
        this.kragsteinpackage_relationship = kragsteinpackage_relationship;
    }

}