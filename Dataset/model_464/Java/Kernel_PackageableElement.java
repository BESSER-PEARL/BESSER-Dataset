





import java.util.List;
import java.util.ArrayList;

public class Kernel_PackageableElement  {






    private fUML_Kernel_Namespace fuml_kernel_namespace;




    private fUML_Kernel_ElementImport fuml_kernel_elementimport;




    private fUML_Kernel_Package fuml_kernel_package;


    public Kernel_PackageableElement(
    ) {
    }



    public fUML_Kernel_Namespace getFuml_kernel_namespace() {
        return fuml_kernel_namespace;
    }

    public void setFuml_kernel_namespace(fUML_Kernel_Namespace fuml_kernel_namespace) {
        this.fuml_kernel_namespace = fuml_kernel_namespace;
    }
    public fUML_Kernel_ElementImport getFuml_kernel_elementimport() {
        return fuml_kernel_elementimport;
    }

    public void setFuml_kernel_elementimport(fUML_Kernel_ElementImport fuml_kernel_elementimport) {
        this.fuml_kernel_elementimport = fuml_kernel_elementimport;
    }
    public fUML_Kernel_Package getFuml_kernel_package() {
        return fuml_kernel_package;
    }

    public void setFuml_kernel_package(fUML_Kernel_Package fuml_kernel_package) {
        this.fuml_kernel_package = fuml_kernel_package;
    }

}