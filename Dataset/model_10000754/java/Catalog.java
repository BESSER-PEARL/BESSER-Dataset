





import java.util.List;
import java.util.ArrayList;

public class Catalog  {






    private book book;




    private OwnBookStorage ownbookstorage;




    private InnerBookStorage innerbookstorage;


    public Catalog(
    ) {
    }



    public book getBook() {
        return book;
    }

    public void setBook(book book) {
        this.book = book;
    }
    public OwnBookStorage getOwnbookstorage() {
        return ownbookstorage;
    }

    public void setOwnbookstorage(OwnBookStorage ownbookstorage) {
        this.ownbookstorage = ownbookstorage;
    }
    public InnerBookStorage getInnerbookstorage() {
        return innerbookstorage;
    }

    public void setInnerbookstorage(InnerBookStorage innerbookstorage) {
        this.innerbookstorage = innerbookstorage;
    }

}