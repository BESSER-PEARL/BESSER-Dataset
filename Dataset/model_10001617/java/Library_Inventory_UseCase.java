





import java.util.List;
import java.util.ArrayList;

public class Library_Inventory_UseCase  {






    private CD_UseCase cd_usecase;




    private Book_UseCase book_usecase;




    private Software_UseCase software_usecase;




    private Video_UseCase video_usecase;


    public Library_Inventory_UseCase(
    ) {
    }



    public CD_UseCase getCd_usecase() {
        return cd_usecase;
    }

    public void setCd_usecase(CD_UseCase cd_usecase) {
        this.cd_usecase = cd_usecase;
    }
    public Book_UseCase getBook_usecase() {
        return book_usecase;
    }

    public void setBook_usecase(Book_UseCase book_usecase) {
        this.book_usecase = book_usecase;
    }
    public Software_UseCase getSoftware_usecase() {
        return software_usecase;
    }

    public void setSoftware_usecase(Software_UseCase software_usecase) {
        this.software_usecase = software_usecase;
    }
    public Video_UseCase getVideo_usecase() {
        return video_usecase;
    }

    public void setVideo_usecase(Video_UseCase video_usecase) {
        this.video_usecase = video_usecase;
    }

}