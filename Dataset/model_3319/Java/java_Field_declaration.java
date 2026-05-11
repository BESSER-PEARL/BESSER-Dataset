





import java.util.List;
import java.util.ArrayList;

public class java_Field_declaration  {

    private String debug;
    private String doc;





    private java_Interface_declaration java_interface_declaration;




    private java_EObject java_eobject;


    public java_Field_declaration(
        String debug,        String doc    ) {
        this.debug = debug;
        this.doc = doc;
    }


    public String getDebug() {
        return debug;
    }

    public void setDebug(String debug) {
        this.debug = debug;
    }
    public String getDoc() {
        return doc;
    }

    public void setDoc(String doc) {
        this.doc = doc;
    }

    public java_Interface_declaration getJava_interface_declaration() {
        return java_interface_declaration;
    }

    public void setJava_interface_declaration(java_Interface_declaration java_interface_declaration) {
        this.java_interface_declaration = java_interface_declaration;
    }
    public java_EObject getJava_eobject() {
        return java_eobject;
    }

    public void setJava_eobject(java_EObject java_eobject) {
        this.java_eobject = java_eobject;
    }

}