





import java.util.List;
import java.util.ArrayList;

public class Chef_Actor  {






    private Food_Serving_UseCase food_serving_usecase;




    private Menu_Preparation_UseCase menu_preparation_usecase;


    public Chef_Actor(
    ) {
    }



    public Food_Serving_UseCase getFood_serving_usecase() {
        return food_serving_usecase;
    }

    public void setFood_serving_usecase(Food_Serving_UseCase food_serving_usecase) {
        this.food_serving_usecase = food_serving_usecase;
    }
    public Menu_Preparation_UseCase getMenu_preparation_usecase() {
        return menu_preparation_usecase;
    }

    public void setMenu_preparation_usecase(Menu_Preparation_UseCase menu_preparation_usecase) {
        this.menu_preparation_usecase = menu_preparation_usecase;
    }

}