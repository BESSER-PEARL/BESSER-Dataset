





import java.util.List;
import java.util.ArrayList;

public class myumlclassdiagram_Package extends NamedElement {






    private List<myumlclassdiagram_Class> myumlclassdiagram_classs;


    public myumlclassdiagram_Package(
    ) {
        super(
        );
        this.myumlclassdiagram_classs = new ArrayList<>();
    }

    public myumlclassdiagram_Package(
        ArrayList<myumlclassdiagram_Class> myumlclassdiagram_classs    ) {
        this.myumlclassdiagram_classs = myumlclassdiagram_classs;
    }


    public List<myumlclassdiagram_Class> getMyumlclassdiagram_classs() {
        return myumlclassdiagram_classs;
    }

    public void addMyumlclassdiagram_class(Myumlclassdiagram_class myumlclassdiagram_class) {
        this.myumlclassdiagram_classs.add(myumlclassdiagram_class);
    }

}