





import java.util.List;
import java.util.ArrayList;

public class simpleany_LibraryType  {






    private List<simpleany_BookType> simpleany_booktypes;




    private simpleany_DocumentRoot simpleany_documentroot;


    public simpleany_LibraryType(
    ) {
        this.simpleany_booktypes = new ArrayList<>();
    }

    public simpleany_LibraryType(
        ArrayList<simpleany_BookType> simpleany_booktypes    ) {
        this.simpleany_booktypes = simpleany_booktypes;
    }


    public List<simpleany_BookType> getSimpleany_booktypes() {
        return simpleany_booktypes;
    }

    public void addSimpleany_booktype(Simpleany_booktype simpleany_booktype) {
        this.simpleany_booktypes.add(simpleany_booktype);
    }
    public simpleany_DocumentRoot getSimpleany_documentroot() {
        return simpleany_documentroot;
    }

    public void setSimpleany_documentroot(simpleany_DocumentRoot simpleany_documentroot) {
        this.simpleany_documentroot = simpleany_documentroot;
    }

}