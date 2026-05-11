





import java.util.List;
import java.util.ArrayList;

public class myDsl_parameter_list_linha  {






    private myDsl_parameter_declaration mydsl_parameter_declaration;




    private List<myDsl_parameter_list_linha> mydsl_parameter_list_linhas;


    public myDsl_parameter_list_linha(
    ) {
        this.mydsl_parameter_list_linhas = new ArrayList<>();
    }

    public myDsl_parameter_list_linha(
        ArrayList<myDsl_parameter_list_linha> mydsl_parameter_list_linhas    ) {
        this.mydsl_parameter_list_linhas = mydsl_parameter_list_linhas;
    }


    public myDsl_parameter_declaration getMydsl_parameter_declaration() {
        return mydsl_parameter_declaration;
    }

    public void setMydsl_parameter_declaration(myDsl_parameter_declaration mydsl_parameter_declaration) {
        this.mydsl_parameter_declaration = mydsl_parameter_declaration;
    }
    public List<myDsl_parameter_list_linha> getMydsl_parameter_list_linhas() {
        return mydsl_parameter_list_linhas;
    }

    public void addMydsl_parameter_list_linha(Mydsl_parameter_list_linha mydsl_parameter_list_linha) {
        this.mydsl_parameter_list_linhas.add(mydsl_parameter_list_linha);
    }

}