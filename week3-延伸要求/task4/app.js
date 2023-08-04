
// 利用fetch連線取得資料
function getData(){
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then(function(response){
        return response.json();
    }).then(function(data){
        console.log(data)
        // //讀取到資料後要做的事，把原本的html重新建立，對上第一週的css
        let main = document.createElement("main");
        document.body.appendChild(main);

        let up= document.createElement("div");
        main.appendChild(up);
        up.setAttribute("class","up")

        let down =document.createElement("div");
        main.appendChild(down);
        down.setAttribute("class","down");

        //讓資料傳進來，遍歷每個區塊

        for(let index=0 ; index< 3; index++){
            //遍歷上方3張
      
            let upCard= document.createElement("div");
            up.appendChild(upCard);
            upCard.setAttribute("class","upCard");

            //圖片區域
            //上方3張圖片
            let img=document.createElement("img");
            upCard.appendChild(img);
        
            //將圖片的網址切到只剩第一個圖片來源
            let myFile=data.result.results[index].file;
            let splits= myFile.split("https");
            let src=`https${splits[1]}`
            img.setAttribute("src",src);

            //文字區域
            let p=document.createElement("p");
            upCard.appendChild(p);
            p.textContent=data.result.results[index].stitle;

        }
        for(let index=3 ; index< 15; index++){
            //遍歷下方12張

            let card=document.createElement("div");
            down.appendChild(card);
            card.setAttribute("class","card");
            
            //圖片區域
            //下方12張圖片
            
            let img=document.createElement("img");
            card.appendChild(img);

            //將圖片的網址切到只剩第一個圖片來源
            let myFile=data.result.results[index].file;
            let splits= myFile.split("https");
            let src=`https${splits[1]}`
            img.setAttribute("src",src);

            //文字區域
            let p=document.createElement("p");
            card.appendChild(p);
            p.textContent=data.result.results[index].stitle;

        }      

    });
};


getData();


function loadData(startIdx) {
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then(function(response){
        return response.json();
    }).then(function(data){
        let main = document.querySelector("main");
        let down = document.querySelector(".down"); 

        
        for (let index = startIdx; index < startIdx + 12 && index < data.result.results.length; index++) {
            let card = document.createElement("div");
            down.appendChild(card);
            card.setAttribute("class", "card");

            // 圖片區域
            // 下方12張圖片

            let img = document.createElement("img");
            card.appendChild(img);

            // 將圖片的網址切到只剩第一個圖片來源
            let myFile = data.result.results[index].file;
            let splits = myFile.split("https");
            let src = `https${splits[1]}`;
            img.setAttribute("src", src);

            // 文字區域
            let p = document.createElement("p");
            card.appendChild(p);
            p.textContent = data.result.results[index].stitle;
        }
    });
};

let load_btn = document.querySelector(".btn");
let startIdx = 15; 

load_btn.addEventListener("click", () => {
    loadData(startIdx); 
    startIdx += 12;
});

//這裡是漢堡圖應用
let hamburger = document.querySelector(".hamburger");
let navitem = document.querySelector(".nav-menu");

hamburger.addEventListener("click",()=>{
    navitem.classList.toggle("active");
})

