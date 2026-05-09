





import java.util.List;
import java.util.ArrayList;

public class library_Author  {

    private String firstname;
    private String secondname;





    private library_Add library_add;




    private library_AddAuthor library_addauthor;


    public library_Author(
        String firstname,        String secondname    ) {
        this.firstname = firstname;
        this.secondname = secondname;
    }


    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getSecondname() {
        return secondname;
    }

    public void setSecondname(String secondname) {
        this.secondname = secondname;
    }

    public library_Add getLibrary_add() {
        return library_add;
    }

    public void setLibrary_add(library_Add library_add) {
        this.library_add = library_add;
    }
    public library_AddAuthor getLibrary_addauthor() {
        return library_addauthor;
    }

    public void setLibrary_addauthor(library_AddAuthor library_addauthor) {
        this.library_addauthor = library_addauthor;
    }

}