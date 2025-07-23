"use client";

import { useState } from "react";
import "./App.css";
import { Toaster, toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover";

function App() {
  // 🧠 상태 정의
  const [manufacturer, setManufacturer] = useState("");
  const [model, setModel] = useState("");
  const [year, setYear] = useState("");
  const [mileage, setMileage] = useState("");

  // 🚀 버튼 클릭 시 실행할 함수
  const handleSubmit = async () => {
    const data = {
      manufacturer,
      model,
      year,
      mileage,
    };

    try {
      const response = await fetch(
        //"http://ec2-13-61-173-216.eu-north-1.compute.amazonaws.com/api/predict-price/predict/",
        "http://localhost:8000/api/predict-price/predict/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        }
      );

      if (!response.ok) throw new Error("서버 오류");

      const result = await response.json();

      toast(`${result.predicted_price}`);
    } catch (err) {
      console.log(err);
      toast("오류", {
        description: "서버와 통신 중 오류가 발생했습니다.",
      });
    }
  };

  return (
    <>
      <Toaster richColors position="top-center" />

      <div className="grid place-items-center h-screen">
        <Popover>
          <PopoverTrigger asChild>
            <Button variant="outline">차량 정보 입력</Button>
          </PopoverTrigger>

          <PopoverContent className="w-80">
            <div className="grid gap-4">
              <div className="space-y-2">
                <h4 className="leading-none font-medium">차량 정보</h4>
              </div>
              <div className="grid gap-2">
                <div className="grid grid-cols-3 items-center gap-4">
                  <Label htmlFor="manufacturer">제조사</Label>
                  <Input
                    id="manufacturer"
                    value={manufacturer}
                    onChange={(e) => setManufacturer(e.target.value)}
                    placeholder="ex) BMW"
                    className="col-span-2 h-8"
                  />
                </div>
                <div className="grid grid-cols-3 items-center gap-4">
                  <Label htmlFor="model">모델명</Label>
                  <Input
                    id="model"
                    value={model}
                    onChange={(e) => setModel(e.target.value)}
                    placeholder="ex) X5 (G05) xDrive 40i xLine"
                    className="col-span-2 h-8"
                  />
                </div>
                <div className="grid grid-cols-3 items-center gap-4">
                  <Label htmlFor="year">연식</Label>
                  <Input
                    id="year"
                    value={year}
                    onChange={(e) => setYear(e.target.value)}
                    placeholder="ex) 23"
                    className="col-span-2 h-8"
                  />
                </div>
                <div className="grid grid-cols-3 items-center gap-4">
                  <Label htmlFor="mileage">주행거리</Label>
                  <Input
                    id="mileage"
                    value={mileage}
                    onChange={(e) => setMileage(e.target.value)}
                    placeholder="ex) 24324"
                    className="col-span-2 h-8"
                  />
                </div>
              </div>
            </div>

            <Button
              variant="outline"
              className="mt-4 w-full"
              onClick={handleSubmit}
            >
              적용
            </Button>
          </PopoverContent>
        </Popover>
      </div>
    </>
  );
}

export default App;
