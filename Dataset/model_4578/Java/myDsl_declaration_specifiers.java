





import java.util.List;
import java.util.ArrayList;

public class myDsl_declaration_specifiers extends parameter_declaration {

    private String Type_qualifier;
    private String Storage_class_specifier;





    private myDsl_type_specifier mydsl_type_specifier;




    private List<myDsl_declaration_specifiers> mydsl_declaration_specifierss;




    private myDsl_declaration_specifiers mydsl_declaration_specifiers;


    public myDsl_declaration_specifiers(
        String Type_qualifier,        String Storage_class_specifier    ) {
        super(
        );
        this.Type_qualifier = Type_qualifier;
        this.Storage_class_specifier = Storage_class_specifier;
        this.mydsl_declaration_specifierss = new ArrayList<>();
    }

    public myDsl_declaration_specifiers(
        String Type_qualifier,        String Storage_class_specifier        ArrayList<myDsl_declaration_specifiers> mydsl_declaration_specifierss    ) {
        this.Type_qualifier = Type_qualifier;
        this.Storage_class_specifier = Storage_class_specifier;
        this.mydsl_declaration_specifierss = mydsl_declaration_specifierss;
    }

    public String getType_qualifier() {
        return Type_qualifier;
    }

    public void setType_qualifier(String Type_qualifier) {
        this.Type_qualifier = Type_qualifier;
    }
    public String getStorage_class_specifier() {
        return Storage_class_specifier;
    }

    public void setStorage_class_specifier(String Storage_class_specifier) {
        this.Storage_class_specifier = Storage_class_specifier;
    }

    public myDsl_type_specifier getMydsl_type_specifier() {
        return mydsl_type_specifier;
    }

    public void setMydsl_type_specifier(myDsl_type_specifier mydsl_type_specifier) {
        this.mydsl_type_specifier = mydsl_type_specifier;
    }
    public List<myDsl_declaration_specifiers> getMydsl_declaration_specifierss() {
        return mydsl_declaration_specifierss;
    }

    public void addMydsl_declaration_specifiers(Mydsl_declaration_specifiers mydsl_declaration_specifiers) {
        this.mydsl_declaration_specifierss.add(mydsl_declaration_specifiers);
    }
    public myDsl_declaration_specifiers getMydsl_declaration_specifiers() {
        return mydsl_declaration_specifiers;
    }

    public void setMydsl_declaration_specifiers(myDsl_declaration_specifiers mydsl_declaration_specifiers) {
        this.mydsl_declaration_specifiers = mydsl_declaration_specifiers;
    }

}