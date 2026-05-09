





import java.util.List;
import java.util.ArrayList;

public class Library_BookOnTape extends AudioVisualItem {






    private Library_Writer library_writer;




    private Library_Person library_person;


    public Library_BookOnTape(
    ) {
        super(
        );
    }



    public Library_Writer getLibrary_writer() {
        return library_writer;
    }

    public void setLibrary_writer(Library_Writer library_writer) {
        this.library_writer = library_writer;
    }
    public Library_Person getLibrary_person() {
        return library_person;
    }

    public void setLibrary_person(Library_Person library_person) {
        this.library_person = library_person;
    }

}