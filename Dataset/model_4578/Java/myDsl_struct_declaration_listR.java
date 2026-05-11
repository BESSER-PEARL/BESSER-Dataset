





import java.util.List;
import java.util.ArrayList;

public class myDsl_struct_declaration_listR  {






    private List<myDsl_struct_declaration_listR> mydsl_struct_declaration_listrs;


    public myDsl_struct_declaration_listR(
    ) {
        this.mydsl_struct_declaration_listrs = new ArrayList<>();
    }

    public myDsl_struct_declaration_listR(
        ArrayList<myDsl_struct_declaration_listR> mydsl_struct_declaration_listrs    ) {
        this.mydsl_struct_declaration_listrs = mydsl_struct_declaration_listrs;
    }


    public List<myDsl_struct_declaration_listR> getMydsl_struct_declaration_listrs() {
        return mydsl_struct_declaration_listrs;
    }

    public void addMydsl_struct_declaration_listr(Mydsl_struct_declaration_listr mydsl_struct_declaration_listr) {
        this.mydsl_struct_declaration_listrs.add(mydsl_struct_declaration_listr);
    }

}