





import java.util.List;
import java.util.ArrayList;

public class MyMouseListener  {

    private String destination;
    private String clickedCard;
    private String temp;
    private String tempCard;
    private boolean singleCardSelected;
    private boolean rightClicked;
    private boolean hasSelected;
    private String source;



    public MyMouseListener(
        String destination,        String clickedCard,        String temp,        String tempCard,        boolean singleCardSelected,        boolean rightClicked,        boolean hasSelected,        String source    ) {
        this.destination = destination;
        this.clickedCard = clickedCard;
        this.temp = temp;
        this.tempCard = tempCard;
        this.singleCardSelected = singleCardSelected;
        this.rightClicked = rightClicked;
        this.hasSelected = hasSelected;
        this.source = source;
    }


    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }
    public String getClickedcard() {
        return clickedCard;
    }

    public void setClickedcard(String clickedCard) {
        this.clickedCard = clickedCard;
    }
    public String getTemp() {
        return temp;
    }

    public void setTemp(String temp) {
        this.temp = temp;
    }
    public String getTempcard() {
        return tempCard;
    }

    public void setTempcard(String tempCard) {
        this.tempCard = tempCard;
    }
    public boolean getSinglecardselected() {
        return singleCardSelected;
    }

    public void setSinglecardselected(boolean singleCardSelected) {
        this.singleCardSelected = singleCardSelected;
    }
    public boolean getRightclicked() {
        return rightClicked;
    }

    public void setRightclicked(boolean rightClicked) {
        this.rightClicked = rightClicked;
    }
    public boolean getHasselected() {
        return hasSelected;
    }

    public void setHasselected(boolean hasSelected) {
        this.hasSelected = hasSelected;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }


}