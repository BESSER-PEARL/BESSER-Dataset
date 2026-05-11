





import java.util.List;
import java.util.ArrayList;

public class simpleJava_interface_declaration  {

    private String nomeInterface;





    private List<simpleJava_name> simplejava_names;


    public simpleJava_interface_declaration(
        String nomeInterface    ) {
        this.nomeInterface = nomeInterface;
        this.simplejava_names = new ArrayList<>();
    }

    public simpleJava_interface_declaration(
        String nomeInterface        ArrayList<simpleJava_name> simplejava_names    ) {
        this.nomeInterface = nomeInterface;
        this.simplejava_names = simplejava_names;
    }

    public String getNomeinterface() {
        return nomeInterface;
    }

    public void setNomeinterface(String nomeInterface) {
        this.nomeInterface = nomeInterface;
    }

    public List<simpleJava_name> getSimplejava_names() {
        return simplejava_names;
    }

    public void addSimplejava_name(Simplejava_name simplejava_name) {
        this.simplejava_names.add(simplejava_name);
    }

}