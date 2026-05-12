





import java.util.List;
import java.util.ArrayList;

public class PlayerView  {

    private None status;
    private None busted;
    private None cardLabels;
    private None moneyBox;
    private None player;
    private None cardTotal;





    private BasePlayer baseplayer;




    private GameView gameview;


    public PlayerView(
        None status,        None busted,        None cardLabels,        None moneyBox,        None player,        None cardTotal    ) {
        this.status = status;
        this.busted = busted;
        this.cardLabels = cardLabels;
        this.moneyBox = moneyBox;
        this.player = player;
        this.cardTotal = cardTotal;
    }


    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public None getBusted() {
        return busted;
    }

    public void setBusted(None busted) {
        this.busted = busted;
    }
    public None getCardlabels() {
        return cardLabels;
    }

    public void setCardlabels(None cardLabels) {
        this.cardLabels = cardLabels;
    }
    public None getMoneybox() {
        return moneyBox;
    }

    public void setMoneybox(None moneyBox) {
        this.moneyBox = moneyBox;
    }
    public None getPlayer() {
        return player;
    }

    public void setPlayer(None player) {
        this.player = player;
    }
    public None getCardtotal() {
        return cardTotal;
    }

    public void setCardtotal(None cardTotal) {
        this.cardTotal = cardTotal;
    }

    public BasePlayer getBaseplayer() {
        return baseplayer;
    }

    public void setBaseplayer(BasePlayer baseplayer) {
        this.baseplayer = baseplayer;
    }
    public GameView getGameview() {
        return gameview;
    }

    public void setGameview(GameView gameview) {
        this.gameview = gameview;
    }

}