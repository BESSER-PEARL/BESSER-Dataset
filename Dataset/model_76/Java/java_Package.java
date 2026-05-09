





import java.util.List;
import java.util.ArrayList;

public class java_Package extends NamedElement {






    private List<java_Package> java_packages;




    private java_Package java_package;


    public java_Package(
    ) {
        super(
        );
        this.java_packages = new ArrayList<>();
    }

    public java_Package(
        ArrayList<java_Package> java_packages    ) {
        this.java_packages = java_packages;
    }


    public List<java_Package> getJava_packages() {
        return java_packages;
    }

    public void addJava_package(Java_package java_package) {
        this.java_packages.add(java_package);
    }
    public java_Package getJava_package() {
        return java_package;
    }

    public void setJava_package(java_Package java_package) {
        this.java_package = java_package;
    }

}