





import java.util.List;
import java.util.ArrayList;

public class Hotel_Guest_Actor  {






    private Check_In_UseCase check_in_usecase;




    private Room_Cleaning_UseCase room_cleaning_usecase;




    private Food_Serving_UseCase food_serving_usecase;




    private Book_Room_UseCase book_room_usecase;




    private Check_Out_UseCase check_out_usecase;


    public Hotel_Guest_Actor(
    ) {
    }



    public Check_In_UseCase getCheck_in_usecase() {
        return check_in_usecase;
    }

    public void setCheck_in_usecase(Check_In_UseCase check_in_usecase) {
        this.check_in_usecase = check_in_usecase;
    }
    public Room_Cleaning_UseCase getRoom_cleaning_usecase() {
        return room_cleaning_usecase;
    }

    public void setRoom_cleaning_usecase(Room_Cleaning_UseCase room_cleaning_usecase) {
        this.room_cleaning_usecase = room_cleaning_usecase;
    }
    public Food_Serving_UseCase getFood_serving_usecase() {
        return food_serving_usecase;
    }

    public void setFood_serving_usecase(Food_Serving_UseCase food_serving_usecase) {
        this.food_serving_usecase = food_serving_usecase;
    }
    public Book_Room_UseCase getBook_room_usecase() {
        return book_room_usecase;
    }

    public void setBook_room_usecase(Book_Room_UseCase book_room_usecase) {
        this.book_room_usecase = book_room_usecase;
    }
    public Check_Out_UseCase getCheck_out_usecase() {
        return check_out_usecase;
    }

    public void setCheck_out_usecase(Check_Out_UseCase check_out_usecase) {
        this.check_out_usecase = check_out_usecase;
    }

}