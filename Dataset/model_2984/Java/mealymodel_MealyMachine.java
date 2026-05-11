





import java.util.List;
import java.util.ArrayList;

public class mealymodel_MealyMachine  {






    private mealymodel_Alphabet mealymodel_alphabet;




    private mealymodel_Alphabet mealymodel_alphabet;




    private List<mealymodel_Transition> mealymodel_transitions;


    public mealymodel_MealyMachine(
    ) {
        this.mealymodel_transitions = new ArrayList<>();
    }

    public mealymodel_MealyMachine(
        ArrayList<mealymodel_Transition> mealymodel_transitions    ) {
        this.mealymodel_transitions = mealymodel_transitions;
    }


    public mealymodel_Alphabet getMealymodel_alphabet() {
        return mealymodel_alphabet;
    }

    public void setMealymodel_alphabet(mealymodel_Alphabet mealymodel_alphabet) {
        this.mealymodel_alphabet = mealymodel_alphabet;
    }
    public mealymodel_Alphabet getMealymodel_alphabet() {
        return mealymodel_alphabet;
    }

    public void setMealymodel_alphabet(mealymodel_Alphabet mealymodel_alphabet) {
        this.mealymodel_alphabet = mealymodel_alphabet;
    }
    public List<mealymodel_Transition> getMealymodel_transitions() {
        return mealymodel_transitions;
    }

    public void addMealymodel_transition(Mealymodel_transition mealymodel_transition) {
        this.mealymodel_transitions.add(mealymodel_transition);
    }

}