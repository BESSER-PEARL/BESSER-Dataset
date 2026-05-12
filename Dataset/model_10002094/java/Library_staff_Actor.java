





import java.util.List;
import java.util.ArrayList;

public class Library_staff_Actor  {






    private Assist_with_research_using_computer_based_tools_UseCase assist_with_research_using_computer_based_tools_usecase;




    private Assist_with_research_using_hard_copy_indexes_UseCase assist_with_research_using_hard_copy_indexes_usecase;




    private Check_in_book_UseCase check_in_book_usecase;


    public Library_staff_Actor(
    ) {
    }



    public Assist_with_research_using_computer_based_tools_UseCase getAssist_with_research_using_computer_based_tools_usecase() {
        return assist_with_research_using_computer_based_tools_usecase;
    }

    public void setAssist_with_research_using_computer_based_tools_usecase(Assist_with_research_using_computer_based_tools_UseCase assist_with_research_using_computer_based_tools_usecase) {
        this.assist_with_research_using_computer_based_tools_usecase = assist_with_research_using_computer_based_tools_usecase;
    }
    public Assist_with_research_using_hard_copy_indexes_UseCase getAssist_with_research_using_hard_copy_indexes_usecase() {
        return assist_with_research_using_hard_copy_indexes_usecase;
    }

    public void setAssist_with_research_using_hard_copy_indexes_usecase(Assist_with_research_using_hard_copy_indexes_UseCase assist_with_research_using_hard_copy_indexes_usecase) {
        this.assist_with_research_using_hard_copy_indexes_usecase = assist_with_research_using_hard_copy_indexes_usecase;
    }
    public Check_in_book_UseCase getCheck_in_book_usecase() {
        return check_in_book_usecase;
    }

    public void setCheck_in_book_usecase(Check_in_book_UseCase check_in_book_usecase) {
        this.check_in_book_usecase = check_in_book_usecase;
    }

}