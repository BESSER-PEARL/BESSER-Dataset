





import java.util.List;
import java.util.ArrayList;

public class library_BookOnTape extends AudioVisualItem {






    private library_Person library_person;




    private library_Writer library_writer;


    public library_BookOnTape(
    ) {
        super(
        );
    }



    public library_Person getLibrary_person() {
        return library_person;
    }

    public void setLibrary_person(library_Person library_person) {
        this.library_person = library_person;
    }
    public library_Writer getLibrary_writer() {
        return library_writer;
    }

    public void setLibrary_writer(library_Writer library_writer) {
        this.library_writer = library_writer;
    }

}